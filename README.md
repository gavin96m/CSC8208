# CSC8208

## Commit Message Format (Angular)
[link](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format)

Brief Summary:
- Commit Message Header
  - **&lt;type>(&lt;scope>): &lt;short summary>**
  - The &lt;type> and &lt;summary> fields are mandatory, the (&lt;scope>) field is optional.
     
&nbsp;
  
- Type
  - Must be one of the following:
    - **docs**: Documentation only changes
    - **feat**: A new feature
    - **fix**: A bug fix
    - **perf**: A code change that improves performance
    - **refactor**: A code change that neither fixes a bug nor adds a feature
    - **test**: Adding missing tests or correcting existing tests
    - **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
    
&nbsp;
    
- Scope
  - The scope should be the name of the classname affected
  
&nbsp;

- Points
  - use the imperative, present tense: "change" not "changed" nor "changes"
  - don't capitalize the first letter 
  - no dot (.) at the end
  