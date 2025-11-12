import scrapy
import re
from scrapy_playwright.page import PageMethod
from ..items import HAItem  # Asegúrate de que tu item HAItem está bien definido
from ..settings import PLAYWRIGHT_MAX_CONTEXTS

class HousinganywhereSpider(scrapy.Spider):
    name = "housinganywhere"
    allowed_domains = ["housinganywhere.com"]

    # Genera URLs de paginación (ajusta el rango según necesites)
    start_urls = [f'https://housinganywhere.com/es/s/Barcelona--Espa%C3%B1a?page={i}' for i in range(1, 4)]
    
    custom_settings = {
        'FEEDS': {
            'data/housinganywhere.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'overwrite': True
            }
        }
    }

    def start_requests(self):
        # 🔹 Dividimos las URLs en 6 grupos (1 por navegador/contexto)
        # num_contexts = 6
        groups = [self.start_urls[i::PLAYWRIGHT_MAX_CONTEXTS] for i in range(PLAYWRIGHT_MAX_CONTEXTS)]

        for i, group in enumerate(groups):
            for url in group:
                yield scrapy.Request(
                    url,
                    meta={
                        "playwright": True,
                        "playwright_context": f"context_{i}",  # 🔹 navegador independiente
                        "playwright_page_methods": [
                            PageMethod("wait_for_selector", "a.css-1efwqj7-cardLink"),
                            PageMethod("evaluate", "window.scrollBy(0, window.innerHeight)"),
                            PageMethod("wait_for_timeout", 300),
                            PageMethod("evaluate", "window.scrollBy(0, window.innerHeight)"),
                            PageMethod("wait_for_timeout", 200),
                            PageMethod("evaluate", "window.scrollBy(0, window.innerHeight)"),
                            PageMethod("wait_for_timeout", 500),
                            PageMethod("evaluate", "window.scrollBy(0, window.innerHeight)"),
                            PageMethod("wait_for_timeout", 3000),
                        ]
                    },
                    callback=self.parse
                )

    def parse(self, response):
        # Extrae enlaces usando el selector CSS (verifica en la web que el selector es correcto)
        links = response.css("a.css-1efwqj7-cardLink::attr(href)").getall()
        self.log(f"Encontrados {len(links)} enlaces en {response.url}")

        for link in links:
            item = HAItem()
            item["url_actual"] = response.url
            # Genera URL absoluta y elimina parámetros si existen
            item["url_inmueble"] = response.urljoin(link).split('?')[0]
            item['title']= link.xpath("//span[re:test(@data-test-locator, 'Listing.*Card.*Title', 'i')]/text()").getall()

            yield item
