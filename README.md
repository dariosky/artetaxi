# Arte Site - rebrand

Based on: [Start Bootstrap - Creative](https://startbootstrap.com/template-overviews/creative/)

## Usage

### Basic Usage

Install all the yarn and Python requirements.

```shell
yarn install
pip install -r requirements
```

Run `gulp dev` to view the site in your browser. Run `gulp` to just run the build.

# Translations

* Change your template files (in the `template folder`), and use the _() function to mark the text
* run `babel.sh` to generete the messages mo files
* call `po2excel` to update the `translations.xlsx`
* Fill the `translations.xlsx`
* when done run `i18n.py` to create the HTMLs out of the templates

#### Gulp Tasks

- `gulp` the default task that builds everything
- `gulp dev` browserSync opens the project in your default browser and live reloads when changes are made

#### Deploy

Push the updates to GITHUB and run

```shell
fab deploy
```
