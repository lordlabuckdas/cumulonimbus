# backend

**stack:** flask + mongodb

## endpoints

* `GET /api`
	* `sort` -> sort key
	  * **default:** `last_seen`
		* options: `["mac_address", "os", "domain", "workgroup", "ip_address", "hostname"]`
	* `asc` -> sort order
		* **default:** descending
		* options: `1` for `ascending`, anything else `descending`
	* `page` -> page number
		* **default:** 1
		* options: 1 -> `size(documents)/MAX_RESULTS_PER_PAGE`
		* `MAX_RESULTS_PER_PAGE` = 5
		* higher-than-possible page number will err out
* `GET /api/search`
	* `category` -> query key
		* **default:** `["mac_address", "os", "domain", "workgroup", "ip_address", "hostname"]`
		* options: any **one** of the above
	* `query` -> query value
	* + *same properties as `/api`*

## setup

```shell
$ pip install -r requirements.txt
$ flask run
```
