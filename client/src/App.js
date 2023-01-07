import React, { useState,useEffect } from 'react'

function App() {
  const [data,setData] = useState([{}])
  let arr = []
  useEffect(()=> {
    fetch("/members").then(
      res => res.json()
    ).then(
      data=>{
        setData(data)
      }
    )
  },[])
  for (var i = 0; i < data.length; i++)
    arr.push(data[i])
    console.log(data[i])
  
  return((arr.map((user,number) =>
  <div key={number}>
    {user[0]}&ensp;
    {user[1]}&ensp;
    {user[2]}&ensp;
    {user[3]}&ensp;
    {user[4]}&ensp;
  </div>))
  )
}
export default App