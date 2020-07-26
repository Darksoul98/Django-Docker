
## Django
#### Assumptions
- If both `pick_first` and `support_multiple` are `true` then `pick_first` result is chosen. 
- `invalid_trigger` value is passed to `trigger` in params
- In case of finite_value_validator :
	- If any value is invalid then params is set to {}
 
In case of numeric_value_validator: 
- if pick_first is true first valid value will be selected.

|       Endpoint    |Method          |
|-------------------|----------------|
|/finite_validation |POST            |
|/numeric_validation|POST            |

## Docker
Image size: 956 MB
### Build
```bash
sudo docker build -t django_app .
```
### Run
```bash
sudo docker run -p 80:8000 -i -t django_app
```
