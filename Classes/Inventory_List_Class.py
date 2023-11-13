from Video_Class import Video


class Inventory_List():

    def __init__(self):
        self.inventory_list = []

    def get_inventory(self):
        return self.inventory_list

    def add_video(self, name, year, director, rating, genre, rentalStatus):
        new_video = Video(name, year, director, rating, genre, rentalStatus)
        self.inventory_list.append(new_video)
        return f'Added: {name} to inventory.'

    def remove_video(self, name):
        for video in self.inventory_list:
            if video.name == name:
                self.inventory_list.remove(video)
                return f'Removed: {name} from inventory.'
        return 'Video not found in inventory'

    def get_inventory_list_by_attribute(self, attribute):
        matching_inventory = []
        for video in self.inventory_list:
            if attribute in video.name or attribute in video.genre or attribute in str(video.year) or attribute in video.director or attribute in str(video.rating):
                matching_inventory.append(video)
        return matching_inventory

    def sort_inventory(self, attribute, order='asc'):
        reverse = False if order == 'asc' else True
        self.inventory_list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)