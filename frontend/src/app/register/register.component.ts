import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { ApiServiceService } from '../api-service.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent implements OnInit {
  fullname: string;
  email: string;
  phone: string;
  datebirth: string;

  constructor(
    private router: Router,
    private apiService: ApiServiceService,
    private toastr: ToastrService
  ) {}

  ngOnInit(): void {}

  register() {
 debugger
    if (this.fullname && this.datebirth && this.email && this.phone) {
      let valid = this.email.search('@');
      if (valid == -1) return this.toastr.error('Invalid email id format.');
      let year1 = new Date(this.datebirth).getFullYear();
      let year2 = new Date().getFullYear();
      let checkDOB = year2 - year1;
      if (checkDOB < 18)
        return this.toastr.error(
          '',
          'Your DOB is not Eligible, Because your Age should be more than 18 years.'
        );
      let data = {
        fullname: this.fullname,
        email:this.email,
        datebirth:this.datebirth,
        phone:this.phone
      };
      this.apiService
        .postMethod('/registration/', data)
        .subscribe((response: any) => {
          if (response.status == 200) {
            this.toastr.success('', 'Register Successfully');
            this.router.navigate(['/listdata']);
          } else {
            this.toastr.error('', response.message);
          }
        });
    } else {
      this.toastr.error('', 'All field required');
    }
  }


  inputKeydown(e) {
    var key = e.keyCode ? e.keyCode : e.which;
    if (!(
      [8, 9, 13, 27, 46, 190].indexOf(key) !== -1 ||
      (key == 65 && (e.ctrlKey || e.metaKey)) ||
      (key >= 35 && key <= 40) ||
      (key >= 48 && key <= 57 && !(e.shiftKey || e.altKey)) ||
      (key >= 96 && key <= 105)
    )) e.preventDefault();
  }
  
}

