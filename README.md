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

- git clone locally:
  ```bash
  git clone git@github.com:ssanj/st-plugin-zat.git CHECKOUT_DIR
  ```
- Run [zat](https://github.com/ssanj/zat):
  ```bash
  zat --target-dir TARGET_DIRECTORY --template-dir CHECKOUT_DIR
  ```

- Enter values for `project` and `plugin description` when prompted. Choose `y` to confirm values

- Make scripts executable:
  ```bash
  chmod +x TARGET_DIRECTORY/run-tests
  chmod +x TARGET_DIRECTORY/compile
  ```
- Run tests with: `./run-tests`
- Compile code with: `./compile`
- Add to Sublime Text by symlinking to your TARGET_DIRECTORY:
  ```bash
  ln -s TARGET_DIRECTORY SUBLIME_TEXT_INSTALLATION/PACKAGES/
  ```

- To verify if your plugin is working, run *SHIFT+CMD+P* and find PLUGIN_NAME and run it. Your PLUGIN_NAME is root folder your TARGET_DIRECTORY.
- Open the console with *CTRL+`*. You should see the following:

```
[PLUGIN_NAME] - your_plugin_name_snake_case is running
[PLUGIN_NAME][DEBUG] - settings: PLUGIN_NAMESetting(debug=True)
```
