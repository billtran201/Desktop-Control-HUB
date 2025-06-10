const { app, BrowserWindow } = require('electron');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        fullscreen: true,
        frame: false,
        resizable: false,
        webPreferences: {
            nodeIntegration: true
        }
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);