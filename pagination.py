class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection = list(collection)
    self.items_per_page = items_per_page
    self.per_page = [self.collection[i:i+self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
    self.pages = len(self.per_page)
      
  
  # returns the number of items within the entire collection
  def item_count(self):
    return len(self.collection)
      
  
  # returns the number of pages
  def page_count(self):
    return self.pages
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
        return len(self.per_page[page_index-1]) if page_index>0 and page_index-1<self.pages else -1
        
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
        # for page, page_content in enumerate(self.per_page):
        #     if item_index in page_content:
        #         return page+1
        # return -1
        return item_index // self.items_per_page if item_index in self.collection else -1

  