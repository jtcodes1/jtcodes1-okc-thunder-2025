import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { BaseService } from './base.service';

@Injectable({
  providedIn: 'root'
})
export class PlayersService extends BaseService {
  constructor(protected http: HttpClient) {
    super(http);
  }

  // Get one player's summary by ID
  getPlayerSummary(playerID: number): Observable<any> {
    const endpoint = `${this.baseUrl}/api/v1/playerSummary/${playerID}`; // matches backend route
    return this.get(endpoint).pipe(
      map((data: Object) => ({
        endpoint: endpoint,
        apiResponse: data
      }))
    );
  }

  // Get all players summary
  getAllPlayers(): Observable<any> {
    const endpoint = `${this.baseUrl}/api/v1/allPlayersSummary`; // matches backend route
    return this.get(endpoint).pipe(
      map((data: Object) => ({
        endpoint: endpoint,
        apiResponse: data
      }))
    );
  }
}
