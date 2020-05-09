package main

type Color struct {
	r, g, b, a uint32
}

//RGBA is a method
func (c Color) RGBA() (r, g, b, a uint32) {
	return c.r, c.g, c.b, c.a
}

var yellowColor Color = Color{0, 255, 0, 0}
