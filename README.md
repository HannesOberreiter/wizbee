# WizBee

![WizBeeLogo](favicon-96x96.png)

Simple answer bot integrated into [b.tree Beekeeping Software](https://www.btree.at) . This repository is a playground, currently the main goal is to upload the markdown documentation to a vector database.

## Setup

As vector database a Docker redis instance is used, see [github.com/HannesOberreiter/btree_database](https://github.com/HannesOberreiter/btree_database).

Our helper tool to create the LLM is Langchain [github.com/hwchase17/langchain/](https://github.com/hwchase17/langchain/).

As AI framework we use [openai.com/](https://openai.com/).

## Structure

- `content` contains the files to upload
- `references_example.json` helper file to reference content files with metadata, needs to be renamed to `references.json`
- `example.env` contains needed API keys and other environment variables, needs to be renamed to `.env`
