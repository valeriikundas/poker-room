package main

type Player struct {
	Username string
	Stack    uint
	Cards    string
}

func NewPlayer(username string, stack uint, cards string) Player {
	return Player{
		Username: username,
		Stack:    stack,
		Cards:    cards,
	}
}
