# List Files Action

GitHub action to list path of all files of a particular extension in the folder/directory
specified by the user.

## Inputs
| Input             | Description                |
|-------------------|----------------------------|
| `path` (required) | Path where searching files |
| `ext`  (required) | File extension to match    |

## Outputs

| Output       | Description                               |
|--------------|-------------------------------------------|
| `paths`      | Paths of all the files with the extension |

## Usage example

```yaml
name: List Files Example

on:
  pull_request:
  workflow_dispatch:

jobs:
  list-files:
    runs-on: ubuntu-latest
    outputs:
      paths: ${{ steps.list-files.outputs.paths }}
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2.4.0
      - name: List Files
        id: list-files
        uses: mirko-felice/list-files@v1.0.2
        with:
          path: "."
          ext: ".yml"
  test:
    needs: list-files
    strategy:
      matrix:
        paths: ${{ fromJson(needs.list-files.outputs.paths) }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2.4.0
      - name: Output results
        run: |
          echo ${{ matrix.paths }}
```
Output generated for the above yaml file (in this repository):

```shell
github/workflows/test.yml
action.yml
```

## License
[MIT license]

[MIT license]: LICENSE