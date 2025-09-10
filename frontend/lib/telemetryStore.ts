// frontend/lib/telemetryStore.ts
"use client";
import { create } from "zustand";

export type Telem = {
  t: number;
  altitude_agl_m: number;
  vertical_speed_mps: number;
  wind_x_mps: number;
  wind_y_mps: number;
  phase?: string;
};

type TelemState = {
  telem: Telem | null;
  setTelem: (t: Telem) => void;
};

export const useTelemStore = create<TelemState>((set) => ({
  telem: null,
  setTelem: (t) => set({ telem: t }),
}));