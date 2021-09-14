import { Component, OnInit } from '@angular/core';
import { GrabDataService } from 'src/services/grab-data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  title: string = '';
  body: string = '';

  constructor(private backend: GrabDataService) {}

  ngOnInit(): void {
    this.backend.getPageData('/home').subscribe(req => {
      let data:any = req;
      this.title = data.title
      this.body = data.body;
    })
  }

}
