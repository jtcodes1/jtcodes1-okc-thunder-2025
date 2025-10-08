import { ChangeDetectorRef, Component, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { untilDestroyed, UntilDestroy } from '@ngneat/until-destroy';
import { PlayersService } from '../_services/players.service';

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {

  players: any[] = [];  // Array to hold all players
  loading: boolean = true;

  constructor(
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
  ) {}

  ngOnInit(): void {
    this.playersService.getAllPlayers() // <-- call service method that returns all players
      .pipe(untilDestroyed(this))
      .subscribe(data => {
        this.players = data.apiResponse || data; // assign all players
        this.loading = false;
        this.cdr.detectChanges();
      }, error => {
        console.error('Error fetching players:', error);
        this.loading = false;
      });
  }

  ngOnDestroy() {}
}
