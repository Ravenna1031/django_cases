import yaml
import pytest

with open("nums.yaml") as f:
    yaml_load = yaml.safe_load(f)
    nums = yaml_load['nums']
    ids = yaml_load['ids']


@pytest.fixture(params=nums, ids=ids)
def get_nums_data(request):
    data = request.param
    yield data