import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {
    apiUrl = "https://ritik55.pythonanywhere.com";

  constructor(
    private http: HttpClient
  ) { }
  
  postMethod(apiname,data){
    return this.http.post(this.apiUrl + apiname, data);
  }


  getMethod(apiname){
    return this.http.get(this.apiUrl + apiname);
  }
}
