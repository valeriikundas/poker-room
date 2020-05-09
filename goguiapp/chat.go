package main

// import (
// 	"log"
// 	"strings"

// 	"fyne.io/fyne"
// 	"fyne.io/fyne/widget"
// )

// type Chat struct {
// 	Entry *widget.Entry
// }

// var text string = `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius lacinia eros, sit amet porta turpis consequat id. Curabitur facilisis id neque in laoreet. Nunc hendrerit dapibus congue. Nam et libero purus. Proin neque odio, fermentum a lacus et, suscipit venenatis risus. Curabitur venenatis lectus id dolor volutpat pellentesque. Fusce consequat enim non gravida varius.
// 	Nam vulputate vehicula nibh, quis consequat massa eleifend sed. Nunc a lorem nibh. Curabitur eget consequat nunc. Maecenas vitae volutpat lectus. Cras vel leo accumsan, maximus quam nec, maximus nibh. Etiam porttitor eu justo non pharetra. Duis ut feugiat sem. Praesent nec dapibus nisl. Cras et lobortis nulla.
// 	Maecenas finibus quam nulla, eget dapibus augue fringilla id. Ut eu lorem id mauris elementum congue nec id turpis. Aenean vitae convallis lacus. Nam consectetur luctus mauris vitae iaculis. Donec pulvinar ante rhoncus, posuere velit vel, tincidunt nibh. Vestibulum sit amet congue arcu. Nunc cursus magna vel felis fermentum, sed eleifend ante dignissim. Duis sodales tellus purus, ac porttitor libero sagittis vel. Donec et dapibus lectus. Proin quis felis vitae metus posuere facilisis. Vestibulum elit odio, consequat gravida enim ac, volutpat finibus turpis. Suspendisse porttitor quis libero eget eleifend. Morbi et diam nulla.`

// func NewChat() *Chat {
// 	entry := widget.NewMultiLineEntry()
// 	return &Chat{Entry: entry}
// }

// func (c *Chat) FocusLost() {
// 	log.Println("focus lost")
// }

// func (c *Chat) FocusGained() {
// 	c.FocusGained()
// 	log.Println("focus gained")
// }

// func (c *Chat) Hide() {
// 	c.Entry.Hidden = true
// }

// func (c *Chat) Show() {
// 	c.Entry.Hidden = false
// }

// func (c *Chat) OnChanged(text string) {
// 	lines := strings.Split(text, "\n")
// 	for i, line := range lines {
// 		if len(line) >= 20 {
// 			newLine := line[20:]
// 			line := line[:20]
// 			lines = append(lines[:i], line, newLine)
// 			lines = append(lines, lines[i+1:]...)
// 		}
// 	}
// 	c.Entry.SetText(strings.Join(lines, "\n"))
// }

// func (c *Chat) TypedKey(key *fyne.KeyEvent) {
// 	c.TypedKey(key)
// }

// func (c *Chat) MinSize() fyne.Size {
// 	return c.Entry.MinSize()
// }

// func (c *Chat) Move(pos fyne.Position) {
// 	c.Entry.Move(pos)
// }

// func (c *Chat) Position() fyne.Position {
// 	return c.Entry.Position()
// }

// func (c *Chat) Resize(size fyne.Size) {
// 	//c.Entry.Resize(size)
// }

// func (c *Chat) Size() fyne.Size {
// 	return c.Entry.Size()
// }

// func (c *Chat) Visible() bool {
// 	return c.Entry.Visible()
// }
