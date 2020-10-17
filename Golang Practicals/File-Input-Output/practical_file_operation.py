package main

import(
	"fmt"
	"os"
	"log"
	"io/ioutil"
)
func main()
{
	file, err:=os.Create("sample.txt")
	if err!=nil
	{
		log.fatal(err)
	}
	file.WriteString("Hi, my name is Priya and this file was created using GO!!")
	file.close()
	
	sttream, err:=ioutil.ReadFile("sample.txt")
	if err!=nil{
		log.fatal(err)
	}
	s1=string(stream)
	fmt.Println(s1)
}