import {useRef } from "react";

export const Search = ({fn})=>{
const productName = useRef();
    return (
        <>
            <label>Product Name </label>     
            <input ref={productName} type= 'text' className="form control"  placeholder = 'Type to search here'/>
            <br></br>
            <button className="btn btn-success" onClick={()=>{
                fn(productName.current.value);
            }}>Search it</button>
            <hr></hr>
        </>
    )
}