package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello from Echo Space! 🚀")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	port = ":" + port
	e.Logger.Fatal(e.Start(port))

}

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello from Space! 🚀")
}
