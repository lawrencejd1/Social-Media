import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GrabDataService {

  constructor(private http: HttpClient) { }

  apiUrl = 'http://127.0.0.1:5000'

  initPageData(page:string){
    return this.http.get(this.apiUrl + page)
  }

  

}
