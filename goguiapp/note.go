package main

import (
	"log"

	"fyne.io/fyne/widget"
)

type NoteField struct {
	*widget.Entry
}

func NewNoteField() *widget.Entry {
	return widget.NewMultiLineEntry()
}

func (noteField *NoteField) FocusGained() {
	log.Println("focus gained")

}

func (noteField *NoteField) FocusLost() {
	log.Println("focus lost")

}

// func (noteField *NoteField) OnChanged(s string) {}
