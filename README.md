# List Files Action

GitHub action to list path of all files of a particular extension in the folder/directory
specified by the user.

## Inputs
| Input                                    | Description                           |
|------------------------------------------|---------------------------------------|
| `repo` (required)                        | Repository name where to search files |
| `ref`  (optional => default is 'master') | Branch or tag to checkout             |
| `path` (required)                        | Path where searching files            |
| `ext`  (required)                        | File extension to match               |

## Outputs

| Output       | Description                               |
|--------------|-------------------------------------------|
| `paths`      | Paths of all the files with the extension |

## Usage example

```yaml
name: Test

on:
  push:
    tags-ignore:
      - '*'
    branches:
      - 'master'
  pull_request:
  workflow_dispatch:

jobs:
  list-files:
    runs-on: ubuntu-latest
    outputs:
      paths: ${{ steps.list-files.outputs.paths }}
    steps:
      - name: List Files
        id: list-files
        uses: mirko-felice/list-files-action@v3.0.0
        with:
          repo: ${{ github.repository }}
          ref: ${{ github.ref_name }}
          path: "."
          ext: ".yml"
  Test:
    needs: list-files
    strategy:
      matrix:
        paths: ${{ fromJson(needs.list-files.outputs.paths) }}
    runs-on: ubuntu-latest
    steps:
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