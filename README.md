# coins-required
Python 2 codes to determine the efficiency of various coin denominations, with data from the Office for National Statistics (ONS) on what people actually spend money on.

Referenced in [*Boring Talks* \#33 - Change](https://www.bbc.co.uk/programmes/p06xvmpz) and [*Forget a new £1 coin, why we need a £1.23 coin*](http://chalkdustmagazine.com/blog/forget-a-new-1-pound-coin-we-need-a-1-pound-23-coin/).

### Scripts without ONS data:

1. `coins_required.py`: Calculates the average number of coins you would need to generate amounts up to `up_to_amount`, assuming that each amount is equally likely. Also generates the average weight of these coins (actual weight, like in kilograms!) if you provide the `weights` as well.

1. `coins_required_which_coins.py`: Calculates the most efficient coins you need to generate amounts up to `up_to_amount`.

2. `coins_required_which_combinations.py`: If you could only pick `use_n_coins` coins out of our current set, which would you pick?

3. `coins_required_which_to_add.py`: If you could only add one coin to our current set, which would you pick?

4. `coins_required_which_to_replace.py`:  If you could replace one coin from our current set with another, which would you pick?

### Scripts using ONS data:

1. `ons_data/coins_ons.py`: Reads in the prices of individual items from shops all over the country, chooses all prices between £0 and £20, and plots the price mod `lowest_banknote` as a percentage of all possible prices. Note that it does *not* weight the item on how commonly bought it is, which is something that is considered in another file.

2. `ons_data/make_baskets.py`: Creates a set of representative shopping baskets and writes them to `baskets2.txt`. The basket is made by (i) working out how commonly an item is bought, then (ii) filling a basket of size `basket_sizes` with items which are chosen randomly but weighted on how commonly they are bought. The price of each item is itself chosen randomly from the prices it is sold at, but weighted on how common that price is.

    - Part (i) is done by working out how commonly an item is bought. It does this by taking CPI weight (how much of consumer income is spent on an item type) and dividing by the average price of an item (mean of all prices this item type is sold at, weighted on how many stores each retailer has): this produces a 'number weight'. High number weights are bought more often.

3. `ons_data/baskets_mod_something.py`: Reads in the prices of the baskets created with `make_baskets.py`, listed in `baskets2.txt`, and plots their prices mod `lowest_banknote` as a percentage of all possible prices

4. `coins_required_with_baskets.py`: Calculates the average number of coins you would need to generate amounts up to `up_to_amount`, using representative baskets from `ons_data/baskets2.txt`. Also generates the average weight of these coins (actual weight, like in kilograms!) if you provide the `weights` as well.

5. `coins_required_which_to_add_with_baskets.py`: Calculates the average number of coins you would need to generate amounts up to `up_to_amount`, using representative
baskets from `ons_data/baskets2.txt`, if you add an extra coin. 

### Data files:

1. `ons_data/price_quote_201807.csv`: This contains individual records of items at various shops, and how much it sells for.

2. `ons_data/item_indices_201807.csv`: Data of how much of consumer income is spent on each item type. Weightings are given in parts per thousand. [ONS](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/consumerpriceinflationupdatingweights/2018): *"The underlying expenditure in each COICOP grouping is converted to an expenditure share relative to total household expenditure for the overall basket and given an integer weight in parts per thousand so that the sum of the weights equals 1,000."*

3. `ons_data/glossary1.xls`: Glossary for the above two data files, provided by the ONS.
