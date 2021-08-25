import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ListdataComponent } from './listdata/listdata.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes = [
  {
    path:'',
    redirectTo:'register',
    pathMatch:"full"
  },
  {
    path:'register',
    component:RegisterComponent
  },
  {
    path:'listdata',
    component:ListdataComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
