import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-listdata',
  templateUrl: './listdata.component.html',
  styleUrls: ['./listdata.component.css']
})
export class ListdataComponent implements OnInit {
  list:any
  constructor(private router: Router,
    private apiService: ApiServiceService,
    private toastr: ToastrService) {
   }

  ngOnInit(): void {
    this.onload()
  }


  onload(){
    debugger
    this.apiService
    .getMethod('/show/')
    .subscribe((response: any) => {
      if (response.status == 200) {
      this.list = response.data
      // console.log(this.list)
      } else {
        this.toastr.error('',"error");
      }
    });
  }
}
