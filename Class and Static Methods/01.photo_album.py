from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    DASHES_COUNT = 11

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]  # lists in list

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):  # iterirame prez albuma, page by page
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:  # ako ima mqsto na stanicata vzimame praznoto mqsto ( slota)
                slot = len(self.photos[page]) + 1  # +1 za da broim stanicite ot 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"
        return "No more free slots"

    def display(self):
        result = [self.DASHES_COUNT * "-"]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASHES_COUNT * "-")

        return "\n".join(result)


album = PhotoAlbum(4)

print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedfdding"))
print(album.add_photo("prvvom"))
print(album.add_photo("wehhdding"))
print(album.add_photo("prdsom"))
print(album.add_photo("wehdding"))
print(album.add_photo("prosdm"))
print(album.add_photo("wedhnding"))
print(album.add_photo("weng"))

print(album.display())
