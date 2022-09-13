from pagination import PaginationHelper

collection = range(1,25)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
helper = PaginationHelper(collection, 10)
print(helper.page_index(-23))
