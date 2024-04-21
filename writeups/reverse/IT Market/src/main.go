package main

import (
	"fmt"
)

const (
	helloMessage = `
	_|_|_|  _|_|_|_|_|  _|      _|                      _|                    _|
	  _|        _|      _|_|  _|_|    _|_|_|  _|  _|_|  _|  _|      _|_|    _|_|_|_|
	  _|        _|      _|  _|  _|  _|    _|  _|_|      _|_|      _|_|_|_|    _|
	  _|        _|      _|      _|  _|    _|  _|        _|  _|    _|          _|
	_|_|_|      _|      _|      _|    _|_|_|  _|        _|    _|    _|_|_|      _|_|
	`

	helpMessage = `
Enter command mode: 
0 - exit
1 - catalog
2 - my products
3 - buy
4 - create product
5 - balance
6 - donate
7 - take a debt
8 - pay the debt`

	maxint = 9223372036854775807
)

var (
	dept     []int    = []int{}
	my       []int    = []int{}
	names    []string = []string{"flag", "Laptop", "Mouse"}
	messages []string = []string{"kxctf{h0h0h0h0_s0_v3ry_cr00k3d_f1ng3r$}", "Here is a laptop", "Here is a mouse"}
	prices   []int    = []int{1337, 50, 50}
	amount   int      = 50
)

func myProducts() {
	fmt.Println()
	if len(my) == 0 {
		fmt.Print("You have no products:((\n")
		return
	}

	fmt.Println("Your products: ")

	for i, indexes := range my {
		fmt.Printf("\t%d. %s :\n\t\t %s\n", i+1, names[indexes], messages[indexes])
	}
	fmt.Println()
}

func balance() {
	fmt.Printf("\nYour balance: %d\n", amount)
}

func list() {
	fmt.Println("\nHere is a product list:")
	for i, _ := range names {
		fmt.Printf("\t%d. %s; price - %d\n", i+1, names[i], prices[i])
	}
}

func takeDept() {
	if len(dept) != 0 {
		fmt.Print("\nYou have a bad reputation, we won't give you a loan!\n")
		return
	}

	fmt.Print("How much money do u want: ")

	var money int
	fmt.Scanf("%d", &money)

	if money < 0 || money > 30 {
		fmt.Print("\nInvalid money!\n")
		return
	}
	dept = append(dept, money)
	amount += money
	fmt.Print("\nYou took a dept!\n")
}

func payDept() {
	if len(dept) == 0 {
		fmt.Print("\nYou no dept!\n")
		return
	}

	amount -= dept[0]
	fmt.Print("\nYou paid a dept!\n")
}

func donate() {
	fmt.Print("How much money do u want to donate: ")

	var money int
	fmt.Scanf("%d", &money)

	if money < 0 || money > 30 {
		fmt.Print("\nInvalid money!\n")
		return
	}

	if money > amount {
		fmt.Print("\nYou have no money!\n")
		return
	}

	amount -= money

	fmt.Print("\nYou successfuly donated!")
}

func buy() {
	list()

	fmt.Print("\nChoose product: ")

	var index int
	fmt.Scanf("%d", &index)

	if index < 1 || index > len(names) {
		fmt.Print("\nInvalid index!\n")
		return
	}

	if prices[index-1] > amount {
		fmt.Print("\nYou have no money!\n")
		return
	}

	my = append(my, index-1)
	amount -= prices[index-1]
	fmt.Print("\nProduct is yours now!\n")
}

func createProduct() {
	var title string
	var message string
	var price int

	fmt.Print("\nProduct name: ")
	fmt.Scanf("%s", &title)

	if len(title) > 10 {
		fmt.Print("\nInvalid name!\n")
		return
	}

	fmt.Print("\nProduct message: ")
	fmt.Scanf("%s", &message)

	if len(message) > 10 {
		fmt.Print("\nInvalid message!\n")
		return
	}

	fmt.Print("\nProduct price: ")
	fmt.Scanf("%d", &price)

	if price < 0 || price > int(float32(maxint)*0.85) {
		fmt.Print("\nInvalid price!\n")
		return
	}

	var realprice int = int(float32(price) / 0.85)

	prices = append(prices, realprice)
	names = append(names, title)
	messages = append(messages, message)

	fmt.Print("\nProduct added! Our store will charge you a commission.\n")

}

func main() {
	fmt.Println(helloMessage)
	var mode int
	exit := false
	for {
		fmt.Println(helpMessage)
		fmt.Print("Enter mode : ")
		fmt.Scanf("%d", &mode)
		switch mode {
		case 1:
			list()
		case 2:
			myProducts()
		case 3:
			buy()
		case 4:
			createProduct()
		case 5:
			balance()
		case 6:
			donate()
		case 7:
			takeDept()
		case 8:
			payDept()
		default:
			fmt.Println("Goodbye!")
			exit = true
		}
		if exit {
			break
		}
	}
}
