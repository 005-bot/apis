<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/capcom/005-bot/tree/main/apis">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">apis</h3>

  <p align="center">
    A reusable API service layer providing data structures and models for Python applications
    <br />
    <a href="https://github.com/capcom/005-bot/tree/main/apis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/capcom/005-bot/tree/main/apis">View Demo</a>
    &middot;
    <a href="https://github.com/capcom/005-bot/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/capcom/005-bot/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The `apis` repository provides a reusable API service layer with standardized data structures and models for Python applications. It includes Pydantic-based models for data validation and serialization, making it easy to maintain consistent data formats across different services.

Key features:
* **Reusable Models**: Common data structures that can be shared across multiple projects
* **Type Safety**: Built with Pydantic for runtime type checking and validation
* **Python 3.11+**: Modern Python features with full type hint support
* **Easy Integration**: Simple installation and usage patterns

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project is built with Python and uses modern development tools:

* [![Python][Python]][Python-url]
* [![Pydantic][Pydantic]][Pydantic-url]
* [![Pipenv][Pipenv]][Pipenv-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.11 or higher
* pipenv for dependency management

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/capcom/005-bot.git
   ```
2. Navigate to the apis directory
   ```sh
   cd 005-bot/apis
   ```
3. Install dependencies using pipenv
   ```sh
   pipenv install
   ```
4. Activate the virtual environment
   ```sh
   pipenv shell
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The `apis` package provides reusable data models that can be imported into your Python applications:

```python
from apis.models import YourModel
from apis.pubsub_models import PubSubMessage

# Use the models in your application
data = YourModel(field1="value1", field2="value2")
```

For more examples and detailed documentation, please refer to the [Documentation](https://github.com/capcom/005-bot/tree/main/apis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Initial project setup with Pydantic models
- [x] Python 3.11+ compatibility
- [ ] Add comprehensive documentation
- [ ] Expand model coverage for additional use cases
- [ ] Add example usage scripts
- [ ] Implement automated testing

See the [open issues](https://github.com/capcom/005-bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Aleksandr Soloshenko - [GitHub Profile](https://github.com/capcom)

Project Link: [https://github.com/capcom/005-bot/tree/main/apis](https://github.com/capcom/005-bot/tree/main/apis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to.

* [Pydantic Documentation](https://docs.pydantic.dev/)
* [Python Packaging User Guide](https://packaging.python.org/)
* [Pipenv Documentation](https://pipenv.pypa.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/capcom/005-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/capcom/005-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/capcom/005-bot.svg?style=for-the-badge
[forks-url]: https://github.com/capcom/005-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/capcom/005-bot.svg?style=for-the-badge
[stars-url]: https://github.com/capcom/005-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/capcom/005-bot.svg?style=for-the-badge
[issues-url]: https://github.com/capcom/005-bot/issues
[license-shield]: https://img.shields.io/github/license/capcom/005-bot.svg?style=for-the-badge
[license-url]: https://github.com/capcom/005-bot/blob/main/apis/LICENSE
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[Pydantic]: https://img.shields.io/badge/pydantic-1.10.13-blue?style=for-the-badge
[Pydantic-url]: https://docs.pydantic.dev/
[Pipenv]: https://img.shields.io/badge/pipenv-2023.10.24-green?style=for-the-badge
[Pipenv-url]: https://pipenv.pypa.io/