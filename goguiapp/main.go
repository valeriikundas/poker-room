package main

import (
	"fmt"
	"image/color"
	"log"
	"strings"

	"fyne.io/fyne"
	"fyne.io/fyne/app"
	"fyne.io/fyne/canvas"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/widget"
)

func main() {
	app := app.New()

	w := app.NewWindow("Hello")
	w.SetFixedSize(true)
	w.Resize(fyne.NewSize(600, 400))

	header := widget.NewLabelWithStyle("Poker Table", 1, fyne.TextStyle{Bold: true})

	players := []Player{
		NewPlayer("darya", 100, "AhKh"),
		NewPlayer("olexandr", 200, "QhQc"),
		NewPlayer("max", 300, "ThTd"),
		NewPlayer("valera", 400, "9sTs"),
	}

	var playerWidgets [4]*widget.Box
	for i, player := range players {
		playerWidgets[i] = widget.NewVBox(
			widget.NewLabel(player.Username),
			widget.NewLabel(player.Cards),
			widget.NewLabel(fmt.Sprintf("%v", player.Stack)))
	}

	//a := make([]fyne.CanvasObject, 4)

	tableWidget := widget.NewHBox()
	for _, playerWidget := range playerWidgets {
		tableWidget.Append(playerWidget)
	}

	progressBar := &widget.ProgressBar{Min: 0, Max: 100, Value: 50}

	actionsContainer := widget.NewVBox(
		widget.NewHBox(
			widget.NewButton("FOLD", func() {
				log.Printf("fold")
			}),
			widget.NewButton("CALL", func() {
				log.Printf("call")
			}),
			widget.NewButton("RAISE", func() {
				size := progressBar.Value
				log.Printf("raise %v", size)
			}),
		),
		progressBar,
	)
	actionsContainer.Move(fyne.Position{X: 500})

	rectangle := canvas.NewRectangle(color.White)
	rectangle.Move(fyne.NewPos(50, 50))
	rectangle.Resize(fyne.NewSize(150, 120))

	//s := "aaaaaaaaa aaaaaaaa aaaaaaaa aaaaaaaaaaaa sdfsdfs"

	chat := widget.NewMultiLineEntry()
	//chat.OnChanged =
	chatTab := chat //fyne.NewContainer(chat)

	notesMap := make(map[string]string)
	for _, player := range players {
		notesMap[player.Username] = ""
	}

	noteField := *widget.NewMultiLineEntry()
	noteField.OnChanged = func(text string) {
		lines := strings.Split(text, "\n")
		var updatedLines []string
		for i, line := range lines {
			if len(line) >= 20 {
				newLine := line[19:]
				line := line[:19]
				updatedLines = lines[:i]
				updatedLines = append(updatedLines, line)
				updatedLines = append(updatedLines, newLine)
				updatedLines = append(updatedLines, lines[i+1:]...)

				chat.CursorRow = chat.CursorRow + 1
				chat.CursorColumn = 1
			} else {
				updatedLines = append(updatedLines, line)
			}
		}

		chat.SetText(strings.Join(updatedLines, "\n"))
	}
	//noteField. #todo: event handling

	playerUsernames := make([]string, 4)
	for i, player := range players {
		playerUsernames[i] = player.Username
	}

	playerSelectField := fyne.NewContainerWithLayout(
		layout.NewHBoxLayout(),
		widget.NewSelect(
			playerUsernames,
			func(username string) {
				noteField.SetText(notesMap[username])
			},
		),
	)

	notesTab := fyne.NewContainerWithLayout(layout.NewVBoxLayout(), playerSelectField, noteField)

	statsTab := widget.NewMultiLineEntry()
	statsTab.SetReadOnly(true)
	statsTab.SetText(fmt.Sprintf("players: %v\n", 4))

	tabs := widget.NewTabContainer(
		widget.NewTabItem("chat", chatTab),
		widget.NewTabItem("notes", notesTab),
		widget.NewTabItem("stats", statsTab),
	)
	bottomPanel := fyne.NewContainerWithLayout(layout.NewGridLayout(2), tabs, actionsContainer)

	layout := layout.NewBorderLayout(header, bottomPanel, nil, nil)
	content := fyne.NewContainerWithLayout(layout, header, bottomPanel, tableWidget)
	w.SetContent(content)

	w.ShowAndRun()
}
