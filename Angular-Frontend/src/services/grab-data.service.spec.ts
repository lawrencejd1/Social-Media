import { TestBed } from '@angular/core/testing';

import { GrabDataService } from './grab-data.service';

describe('GrabDataService', () => {
  let service: GrabDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GrabDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
