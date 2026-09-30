Egy víztorony szabályozása: A projekt célja egy szívattyú be- és kikapcsolása, hogy a víztorony a kívánt töltöttségi tartományban maradjon 30-tól 80%-ig. Ezáltal a lakosság megfelelő víznyomáson kapják az ívóvizet (3-4 bar).
<img width="1223" height="1033" alt="water_level_node Épp bekapcsol a szívattyú majd kikapcsol" src="https://github.com/user-attachments/assets/65049b0f-f778-4a6d-8b82-68d79f5dfa55" />
<img width="1223" height="691" alt="pump_controller Épp bekapcsol a szívattyú majd kikapcsol" src="https://github.com/user-attachments/assets/26c8605d-b928-489f-8c00-0dcc1ccc5df9" />
```mermaid
graph LR
    %% Node-ok és Topic-ok stílusának definiálása
    classDef nodeStyle fill:#2374ab,stroke:#1b5a84,stroke-width:2px,color:#fff,font-weight:bold;
    classDef topicStyle fill:#e6f8ff,stroke:#4cb5ff,stroke-width:1px,stroke-dasharray: 3 3,color:#004b80;

    %% Fő elemek létrehozása
    WL_NODE[water_level_node]:::nodeStyle
    PUMP_CTRL[pump_controller]:::nodeStyle
    
    TOPIC_LEVEL((/water_level)):::topicStyle
    TOPIC_CMD((/pump_command)):::topicStyle

    %% Adatfolyam és irányok (Publisher -> Topic -> Subscriber)
    WL_NODE -->|Publish| TOPIC_LEVEL
    TOPIC_LEVEL -->|Subscribe| PUMP_CTRL

    PUMP_CTRL -->|Publish| TOPIC_CMD
    TOPIC_CMD -->|Subscribe| WL_NODE

    %% Logikai megjegyzések az ábra alatt/mellett
    subgraph Logika és Küszöbértékek
        PUMP_CTRL -.->|Ha vízszint < 30%| BE[Szivattyú BE]
        PUMP_CTRL -.->|Ha vízszint > 80%| KI[Szivattyú KI]
    end

    %% Megjegyzés dobozok színezése
    classDef logicStyle fill:#fff9e6,stroke:#ffe0b2,color:#5d4037;
    class BE,KI logicStyle;
```
