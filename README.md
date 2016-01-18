## Data
Thei dataset defines countries and territories frequently used across many other datasets. It also contains the alias mapping used by gapminder to join data using different country ids, spellings and common typos.

## How to update
Manually edited csv files.

### ddf--alias_mapping--country.csv
The first column contains the gapminder-id (lower case 3-digit iso) The second column contains an alias. This means the same country appears on multiple rows.
#### Adding another alias
If you find a new name or spelling of a country name, please add one more row to the file. 
#### Using the alias mapping
External datasets are joined with matching rows of the alias column and mapped to the geo-id in the geo column.

## License
Gapmidner created this dataset and provides it under [Creative Common Attribution 4.0 International][CC].