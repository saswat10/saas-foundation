from typing import Any
from django.core.management.base import BaseCommand
import helpers
from django.conf import settings

STATIC_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR') 

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.5.2/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.5.2/flowbite.min.js"
}


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading Vendor Files...")

        compeleted_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATIC_VENDOR_DIR/ name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                compeleted_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to Download the {url}")
                )

        if set(compeleted_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS(f"Successfully downloaded the vendor files")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Some files were not downloaded")
            )