# Applications parser for [hh.ru](https://hh.ru)

Current MVP version of the script uses <b>Selenium Chrome driver</b> to go through vacancies you have applied to and form a table with the following structure:

one row = one vacancy
- <b>name</b> - title of the vacancy (position you applied to)
- <b>xp_req</b> - experience requirements specified by the employer in the dedicated field, e.g. 1-3 years
- <b>remote</b> - work format specified by the employer in the dedicated field, which includes time format and possibility of remote work
- <b>company</b> - employer name
- <b>description</b> - description for the vacancy

During the initial script execution you will have to manually imput your email and password at hh.ru, as well as possibly solve the CAPTCHA, 
however after the first successful login your authorization cookies will be saved and used for later sessions.

### Files
<b>hh_parser</b> is the driver function which declares the process of parsing itself.
<b>parsing_processor</b> is the executing script which initializes the parser function and forms the resulting file.
Data is currently stored as a json to facilitate post-processing, which will definitely be needed.


As mentioned earlier, this is just an MVP version of the script, which is why the backlog at the moment contains major features:
- automate the process of getting rid of html tags in the fields 
- form a pipeline to extract semantics of descriptions for further statistical analysis
- implement parallelization of the parsing process to speed up this stage
