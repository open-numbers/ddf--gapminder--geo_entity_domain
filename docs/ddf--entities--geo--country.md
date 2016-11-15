# Countries
This entity set contains a selection of countries and a small selection of other regions.

## Entities

The selection of countries and regions in this file are chosen by Gapminder. We gather both current and historical data. Thus, our country list includes countries which have ceased to exist such as the USSR and Yugoslavia.

## Entity properties

### geo
Gapminder's own identifier for geographic entities. Loosely based on existing standards.

### gwid
Legacy country codes as used by Gapminder World.

### iso3166_1_alpha2, iso3166_1_alpha3, iso3166_1_numeric
These are the country codes as defined in the [ISO 3166-1 standard](https://en.wikipedia.org/wiki/ISO_3166-1). An empty value means there is no ISO 3166-1 code available for this entity.

### iso3166_2
These are the country subdivision codes as defined in the [ISO 3166-2 standard](https://en.wikipedia.org/wiki/ISO_3166-2). An empty value means there is no ISO 3166-2 code available for this entity.

### unicode_region_subtag
These are the country codes as used in the [Unicode Common Locale Data Repository](http://cldr.unicode.org/) (CLDR). Valid tags are defined in [Unicode TR35](http://www.unicode.org/reports/tr35/tr35.html#unicode_region_subtag_validity) and follow mostly the definition of the [BCP47 region subtag](<https://tools.ietf.org/html/bcp47#section-2.2.4>). An empty value means there is no valid region sub-tag for this entity in the CLDR. 

Some sub-tags are [deprecated](<http://unicode.org/reports/tr35/tr35-info.html#Supplemental_Deprecated_Information>), such as the Soviet Union (SU) and are thus not included. They may be included later since the CLDR does contain [data](<http://www.unicode.org/cldr/charts/latest/supplemental/detailed_territory_currency_information.html#SU>) about them.

The unicode_region_subtag overlaps mostly with ISO 3166-1 alpha-2 but contains some additional tags as described in the definition.

This property is used for mapping translations from the CLDR to the entities.

### gapminder_list, alternative_1, alternative_2, alternative_3, alternative_4_cdiac, pandg, god_id, alt_5, upper_case_name, arb1, arb2, arb3, arb4, arb5, arb6
Synonyms for country names gathered from merging legacy country lists in Gapminder. 

These, combined with the ISO and Unicode country codes, are used by recipes to map country names in other data sources to Gapminder geo entities.