import { Routes } from '@angular/router';
import { ExploreComponent } from './pages/explore/explore.component';
import { UserSightingsComponent } from './pages/user-sightings/user-sightings.component';

export const routes: Routes = [
  { path: '', redirectTo: '/explore', pathMatch: 'full' },
  { path: 'explore', component: ExploreComponent },
  { path: 'user-sightings', component: UserSightingsComponent },
  { path: '**', redirectTo: '/explore' }
];
