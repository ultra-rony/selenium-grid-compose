# selenium-grid-compose

This project provides a fully configured setup for running parallel UI tests using Selenium WebDriver and Grid. It's designed to simplify the development and execution of automated browser tests with support for multiple browsers and versions out of the box.

## Getting Started

1. Clone the repository
```bash
git clone https://github.com/ultra-rony/selenium-grid-compose.git
```
2. Navigate into the project directory
```bash
cd selenium-grid-compose
```
3. Start the Docker containers (build if needed)
```bash
docker-compose up --build
```

VNC Viewer for Chrome Browser (if enabled) `http://localhost:7900/`. default password `secret`

Selenium Grid Dashboard
`http://localhost:4444/`

## Examples
<div style="text-align: center">
    <table>
        <tr>         
            <td style="text-align: center">
                <img src="https://github.com/ultra-rony/selenium-grid-compose/blob/main/screens/1.png?raw=true" width="300" alt="">
            </td>
            <td style="text-align: center">
                <img src="https://github.com/ultra-rony/selenium-grid-compose/blob/main/screens/2.png?raw=true" width="300" alt="">
            </td>
            <td style="text-align: center">
                <img src="https://github.com/ultra-rony/selenium-grid-compose/blob/main/screens/3.png?raw=true" width="300" alt="">
            </td>
            <td style="text-align: center">
                <img src="https://github.com/ultra-rony/selenium-grid-compose/blob/main/screens/4.png?raw=true" width="300" alt="">
            </td>
        </tr>
    </table>
</div>