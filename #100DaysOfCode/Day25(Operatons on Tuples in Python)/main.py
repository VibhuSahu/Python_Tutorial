>>> countries = ("Spain", "Italy", "India", "England", "Germany")
>>>
>>> temp = list(countries)
>>> temp.append("Russia")
>>> temp.pop(3)
'England'
>>> temp[2] = "Finland"
>>> countries = tuple(temp)
>>> countries
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
>>>
>>> countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
>>> countries2 = ("Vietnam", "India", "China")
>>> southEastAsia = countries1 + countries2
>>> southEastAsia
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
>>>
>>>
>>> tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
>>> tuple1.count(3)
3
>>> tuple1.index(3)
3
>>> tuple1.index(3, 4, 8)
5
>>> len(tuple1)
9
