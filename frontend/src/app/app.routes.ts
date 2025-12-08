import { Routes } from '@angular/router';
import { AboutPage } from './pages/about-page/about-page';
import { MySightingsPage } from './pages/my-sightings-page/my-sightings-page';
import { ExplorePage } from './pages/explore-page/explore-page';

export const routes: Routes = [
    { path: '', redirectTo: 'explore', pathMatch: 'full' },
    { path: 'explore', component: ExplorePage },
    { path: 'my-sightings', component: MySightingsPage },
    { path: 'about', component: AboutPage },
];
