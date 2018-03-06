import P4_this

def print_sorted_spis(spis):
    for element in spis:
        print('{} = {}'.format(element[0] if element[0] != '\n' else '\\n', element[1]))
    print

text = P4_this.this()
symbols_dict = {}

for symbol in text:
    symbols_dict[symbol] = 1 if symbol not in symbols_dict.keys() else symbols_dict[symbol] + 1

items_symbol_dict = symbols_dict.items()

# alphabetically
items_symbol_dict = sorted(items_symbol_dict, key = lambda x: x[0])
print_sorted_spis(items_symbol_dict)

# in ascending order
items_symbol_dict = sorted(items_symbol_dict, key = lambda x: x[1])
print_sorted_spis(items_symbol_dict)

# in descending order
print_sorted_spis(items_symbol_dict[-1:0:-1])