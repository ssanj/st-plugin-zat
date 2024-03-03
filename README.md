# Simple Sublime Text Plugin Template

Includes the following:

- A default `sublime-commands` file
- A default `sublime-settings` file
- A default `sublime-keymaps` file
- A default `sublime-menu` file for editing settings
- A `tests` folder with a sample test
- A `typings` folder with type hints for the plugin API
- script to run tests (`run-tests`)
- script to compile types (`compile`)


## Installation

### Run remotely

Run remote repository via [zat](https://github.com/ssanj/zat):

```bash
zat process-remote --repository-url https://github.com/ssanj/st-plugin-zat --target-dir TARGET_DIRECTORY
```

### Run locally

Git clone locally:
```bash
git clone git@github.com:ssanj/st-plugin-zat.git TEMPLATE_DIRECTORY
```

Run local template via zat:
```bash
zat --repository-dir TEMPLATE_DIRECTORY --target-dir TARGET_DIRECTORY
  ```

Note: Ensure your `TARGET_DIRECTORY` matches the name of your `project` value below to ensure `compile` has the correct
package structure. If these diverge, manually update the `compile` scripts package structure.

For example, to create a plugin named `MyPlugin`, the TARGET_DIRECTORY should be `SOME_PATH/MyPlugin` and the `project`
name should be `MyPlugin`.

## Configuration


- Enter the following values when prompted:
  - `project` (Name of plugin. This will be CamelCased for Python classes and SnakeCased for file names),
  - `plugin description` (Short description of the plugin in the README.md)
  - `python_version` (Python version used by ST)
  - `command_type` (Command type: one of Text, Window or Application).

Choose `y` to confirm values. Additional variables can be defined in `.variables.zat-prompt` as required.

## Usage

### Prerequisites

Ensure the following tools are installed and on your `PATH`:

- [mypy](https://mypy.readthedocs.io/en/latest/getting_started.html#installing-and-running-mypy) for type checking
- [chokidar-cli](https://github.com/open-cli-tools/chokidar-cli) for monitoring file changes

### Scripts

- Run tests with: `./run-tests`
- Compile code with: `./compile`

### Adding your plugin to Sublime Text

Add your plugin to Sublime Text by symlinking to your TARGET_DIRECTORY:
```bash
ln -s CHECKOUT_DIR SUBLIME_TEXT_INSTALLATION/PACKAGES/
```

## Verification

- To verify if your plugin is working, run *SHIFT+CMD+P* and find PLUGIN_NAME and run it. Your PLUGIN_NAME is the value you entered for `project` converted to CamelCase.
- Open the console with *CTRL+`*. You should see the following:

```
PLUING_NAME COMMAND_TYPE command has loaded.
[PLUGIN_NAME] - your_plugin_name_snake_case is running
[PLUGIN_NAME][DEBUG] - settings: PLUGIN_NAMESetting(debug=True)
```
