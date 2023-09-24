import { Search } from "../components/Search"
import { Songs } from "../components/Items";
import { getSongs } from "../services/api.client";

 export const SearchPage = ()=>{
    const getProductName = (getProductName)=>{
        console.log('Rec Artist Name ', getProductName);
        getSongs(getProductName)
    }
    return(
        <div className="container">
        <h1 className="alert alert-info text-center">Price Checkers</h1>
        <Search fn = {getProductName}/>
        <Songs/>
    </div>); 
 }