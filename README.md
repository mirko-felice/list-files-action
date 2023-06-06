# List Files Action

<p align="center">

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/mirko-felice/list-files-action?label=latest-release)](https://github.com/mirko-felice/list-files-action/releases/latest)

[![Test](https://github.com/mirko-felice/list-files-action/actions/workflows/test.yml/badge.svg)](https://github.com/mirko-felice/list-files-action/actions/workflows/test.yml)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mirko-felice_list-files-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=mirko-felice_list-files-action)
</p>
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
        uses: mirko-felice/list-files-action@v3.0.5
        with:
          repo: ${{ github.repository }}
          ref: ${{ github.ref }}
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