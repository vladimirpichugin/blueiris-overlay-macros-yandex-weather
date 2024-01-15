# Blue Iris Overlay Macros (Yandex Weather)
#### This project is created to contribute to the community. 

<br>Blue Iris: https://blueirissoftware.com/<br>
<i>Blue Iris Tools not required.</i>

Instructions:
1. Download the latest version for Windows from [releases](https://github.com/vladimirpichugin/blueiris-overlay-macros-yandex-weather/releases/tag/latest). 
2. Run the program to create the config.json.
3. [Obtain a personal API key](https://yandex.ru/dev/weather/doc/dg/concepts/about.html) for the Yandex Weather API to work.
4. Update the config.json by setting the API key and specifying a file-location to write a txt file with the weather forecast.
5. Use Windows Task Scheduler to customize the startup time.

Build command:<br>
`pyinstaller --noconfirm --onefile --windowed --name "Blue Iris Weather"  "main.py"`
