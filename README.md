# Supply Chain Data Analysis with Langchain and PandasAI

This project demonstrates how to use Langchain, VertexAI, and PandasAI to fetch and analyze supply chain data from BigQuery, generate answers to questions using a language model, and visualize the data using graphs.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Tools and Libraries](#tools-and-libraries)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Supply chains involve complex data and processes that require efficient data retrieval, analysis, and visualization. This project showcases the use of Langchain, VertexAI, and PandasAI to achieve these tasks seamlessly. The code fetches data from BigQuery, uses a language model to generate answers to queries, and provides data visualization for better insights.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/RahulArora2000/BigQuery-Tables-Analysis-with-Visuals-LangChain.git
   ```

2. Install the required libraries and dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google Cloud credentials by exporting the path to your JSON key file:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/supply-chain-twin-credentials.json
   ```

4. Modify the `supply_data` function in `main.py` to suit your specific data and questions.

## Usage

Run the main script to fetch data from BigQuery, generate answers, and display visualizations:

```bash
python main.py
```

Follow the prompts to input questions and queries about the supply chain data.

## Tools and Libraries

- **Langchain:** Langchain is used for managing data processing pipelines, chaining operations, and integrating language models into data analysis workflows.

- **VertexAI:** VertexAI provides access to AI models for natural language processing. The `VertexAIEmbeddings` and `VertexAI` classes are used for embedding and generating text-based responses.

- **PandasAI:** PandasAI is utilized for interacting with Pandas DataFrames and integrating them with Langchain operations.

- **Google BigQuery:** The code leverages Google BigQuery to fetch supply chain data for analysis.

- **Matplotlib:** Matplotlib is used for generating data visualizations like graphs and charts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

When contributing to this repository, please first discuss the change you wish to make via issue before making any changes. Please follow the code of conduct in all interactions.

## License

This project is licensed under the [MIT License](LICENSE).
```

This `README.md` file provides an overview of the project, installation instructions, usage guidelines, information about the tools and libraries used, and instructions for contributing. You can customize it further to fit your project's specific details and requirements.
