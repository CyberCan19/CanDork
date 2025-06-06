import requests
from bs4 import BeautifulSoup
import openpyxl

print("""

 ██████╗ █████╗ ███╗   ██╗██████╗  ██████╗ ██████╗ ██╗  ██╗          https://instagram.com/canbicer19_
██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝          https://canpersonal.com.tr
██║     ███████║██╔██╗ ██║██║  ██║██║   ██║██████╔╝█████╔╝           https://lwa.com.tr
██║     ██╔══██║██║╚██╗██║██║  ██║██║   ██║██╔══██╗██╔═██╗ 
╚██████╗██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                           
""")

def scrape_google_links(query_url, num_pages):
    all_links = set()

    for page in range(1, num_pages + 1):
        page_url = f"{query_url}&start={(page - 1) * 10}"
        response = requests.get(page_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for anchor in soup.find_all('a'):
                href = anchor.get('href')
                if href.startswith('/url?q='):
                    link = href[7:href.find('&')]
                    all_links.add(link)

    return all_links

def main():
    query = input("Can@Kali-->Arama sorgusunu girin: ")
    num_pages = int(input("root@Kali-->Araştırılacak sayfa sayısını girin: "))
    url = f"https://www.google.com/search?q={query}"

    links = scrape_google_links(url, num_pages)

    if links:
        output_file = input("Can@Kali-->Çıktı dosya adını girin (uzantısı olmadan): ")
        output_format = input("root@Kali-->Çıktı formatını girin (txt veya excel): ")

        if output_format == 'txt':
            with open(f"{output_file}.txt", 'w') as file:
                for link in links:
                    file.write(link + '\n')
            print("Links saved to a txt file.")

        elif output_format == 'excel':
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "Links"

            for index, link in enumerate(links, start=1):
                ws.cell(row=index, column=1, value=link)

            excel_file = f"{output_file}.xlsx"
            wb.save(excel_file)
            print(f"Links saved to an Excel file: {excel_file}")

        else:
            print("Invalid output format. Supported formats: txt or excel.")

    else:
        print("No links found.")

if __name__ == "__main__":
    main()
